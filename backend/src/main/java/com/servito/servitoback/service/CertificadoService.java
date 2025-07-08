package com.servito.servitoback.service;

import com.servito.servitoback.model.Usuario;
import com.servito.servitoback.model.Certificado;
import com.servito.servitoback.repository.CertificadoRepository;
import jakarta.persistence.EntityNotFoundException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
public class CertificadoService {

  @Autowired
  private CertificadoRepository certificadoRepository;

  @Autowired
  private UsuarioService usuarioService;

  public Certificado createCertificado(Certificado certificado) {
    if (!validateCertificado(certificado)) throw new IllegalArgumentException("Certificado inválido");

    Usuario usuario = usuarioService.getUserById(certificado.getUsuario().getId());

    if (usuario == null) {
      throw new EntityNotFoundException("Usuário não encontrado.");
    }

    Certificado certificadoSalvo = certificadoRepository.save(certificado);
    certificadoSalvo.setUsuario(usuario);

    return certificadoRepository.save(certificadoSalvo);
  }

  public Certificado getCertificadoById(Long id) {
    return certificadoRepository.findById(id).orElseThrow(() -> new EntityNotFoundException("Certificado com ID " + id + " não encontrado."));
  }

  public List<Certificado> getCertificadoListByUserId(Long userId) {
    Usuario usuario = usuarioService.getUserById(userId);
    if (usuario == null) {
      throw new EntityNotFoundException("Usuário com ID " + userId + " não encontrado.");
    }
    List<Certificado> certificados = certificadoRepository.findByUsuario(usuario);
    if (certificados.isEmpty()) {
      throw new EntityNotFoundException("Nenhum certificado encontrado para o usuário com ID " + userId + ".");
    } else {
      return certificados;
    }
  }

  public List<Certificado> getCertificadosPendentes() {
    List<Certificado> certificadosPendentes = certificadoRepository.findAll();
    certificadosPendentes.removeIf(certificado -> !certificado.getPendente());
    if (certificadosPendentes.isEmpty()) {
      throw new EntityNotFoundException("Nenhum certificado pendente encontrado.");
    } else {
      return certificadosPendentes;
    }
  }

  @Transactional
  public Certificado updateCertificado(Certificado certificado) {
    if (!validateCertificado(certificado)) throw new IllegalArgumentException("Certificado inválido");

    Certificado certificadoExistente = this.getCertificadoById(certificado.getId());

    copiarDadosCertificado(certificadoExistente, certificado);

    return certificadoRepository.save(certificadoExistente);
  }

  private void copiarDadosCertificado(Certificado destino, Certificado origem) {
    destino.setTitulo(origem.getTitulo());
    destino.setInstituicao(origem.getInstituicao());
    destino.setData(origem.getData());
    destino.setLink(origem.getLink());
    destino.setPendente(origem.getPendente());
    destino.setAprovado(origem.getAprovado());
  }

  public boolean validateCertificado(Certificado certificado) {
    if (certificado == null) return false;
    if (certificado.getTitulo() == null || certificado.getTitulo().isEmpty()) return false;
    if (certificado.getInstituicao() == null || certificado.getInstituicao().isEmpty()) return false;
    if (certificado.getData() == null) return false;
    if (certificado.getLink() == null || certificado.getLink().isEmpty()) return false;
    return true;
  }

  @Transactional
  public void deleteCertificado(Long id) {
    Certificado certificado = this.getCertificadoById(id);
    if (certificado == null) {
      throw new EntityNotFoundException("Certificado com ID " + id + " não encontrado.");
    } else {
      certificadoRepository.deleteById(id);
    }
  }
}
