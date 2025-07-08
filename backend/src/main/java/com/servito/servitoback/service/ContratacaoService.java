package com.servito.servitoback.service;

import com.servito.servitoback.model.Contratacao;
import com.servito.servitoback.repository.ContratacaoRepository;
import jakarta.persistence.EntityNotFoundException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
public class ContratacaoService {
  
  @Autowired
  private ContratacaoRepository contratacaoRepository;

  @Autowired
  private UsuarioService usuarioService;

  @Autowired
  private AnuncioService anuncioService;

  public Contratacao createContratacao(Contratacao contratacao) {
    if (!validateContratacao(contratacao)) {
      throw new IllegalArgumentException("Contratação inválida");
    }

    Contratacao contratacaoSalva = contratacaoRepository.save(contratacao);

    return contratacaoRepository.save(contratacaoSalva);
  }

  public Contratacao getContratacaoById(Long id) {
    return contratacaoRepository.findById(id).orElseThrow(() -> new EntityNotFoundException("Contratação com ID " + id + " não encontrada."));
  }

  public List<Contratacao> getContratacaoListByPrestador(Long prestadorId) {
    if (prestadorId == null) {
      throw new IllegalArgumentException("ID do prestador não pode ser nulo.");
    }
    List<Contratacao> contratacoes = contratacaoRepository.findByPrestador(usuarioService.getUserById(prestadorId));
    if (contratacoes.isEmpty()) {
      throw new EntityNotFoundException("Nenhuma contratação encontrada para o prestador com ID " + prestadorId + ".");
    } else {
      return contratacoes;
    }
  }

  public List<Contratacao> getContratacaoListByContratante(Long contratanteId) {
    if (contratanteId == null) {
      throw new IllegalArgumentException("ID do contratante não pode ser nulo.");
    }
    List<Contratacao> contratacoes = contratacaoRepository.findByContratante(usuarioService.getUserById(contratanteId));
    if (contratacoes.isEmpty()) {
      throw new EntityNotFoundException("Nenhuma contratação encontrada para o prestador com ID " + contratanteId + ".");
    } else {
      return contratacoes;
    }
  }

  public List<Contratacao> getContratacaoListByAnuncio(Long anuncioId) {
    if (anuncioId == null) {
      throw new IllegalArgumentException("ID do anuncio não pode ser nulo.");
    }
    List<Contratacao> contratacoes = contratacaoRepository.findByAnuncio(anuncioService.getAnuncioById(anuncioId));
    if (contratacoes.isEmpty()) {
      throw new EntityNotFoundException("Nenhuma contratação encontrada para o prestador com ID " + anuncioId + ".");
    } else {
      return contratacoes;
    }
  }

  @Transactional
  public Contratacao updateContratacao(Contratacao contratacao) {
    if (!validateContratacao(contratacao)) {
      throw new IllegalArgumentException("Contratação inválida");
    }

    Contratacao contratacaoExistente = this.getContratacaoById(contratacao.getId());

    copiarDadosContratacao(contratacaoExistente, contratacao);

    return contratacaoRepository.save(contratacaoExistente);
  }

  private void copiarDadosContratacao(Contratacao destino, Contratacao origem) {
    destino.setPreco(origem.getPreco());
    destino.setPrazo(origem.getPrazo());
    destino.setDescricao(origem.getDescricao());
    destino.setAceita(origem.getAceita());
    destino.setFinalizada(origem.getFinalizada());
    destino.setPrestador(usuarioService.getUserById(origem.getPrestador().getId()));
    destino.setContratante(usuarioService.getUserById(origem.getContratante().getId()));
    destino.setAnuncio(anuncioService.getAnuncioById(origem.getAnuncio().getId()));
  }

  public boolean validateContratacao(Contratacao contratacao) {
    if (contratacao == null) return false;
    if (contratacao.getPreco() == null || contratacao.getPreco() <= 0) return false;
    if (contratacao.getPrazo() == null || contratacao.getPrazo().isEmpty()) return false;
    if (contratacao.getDescricao() == null || contratacao.getDescricao().isEmpty()) return false;
    if (contratacao.getPrestador() == null || contratacao.getContratante() == null || contratacao.getAnuncio() == null) return false;

    return true;
  }

  @Transactional
  public void deleteContratacao(Long id) {
    Contratacao contratacao = getContratacaoById(id);
    if (contratacao == null) {
      throw new EntityNotFoundException("Contratação com ID " + id + " não encontrada.");
    }
    contratacaoRepository.deleteById(id);
  }
}
