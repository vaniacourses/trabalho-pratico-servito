package com.servito.servitoback.service;

import com.servito.servitoback.model.Usuario;
import com.servito.servitoback.model.Anuncio;
import com.servito.servitoback.repository.AnuncioRepository;
import jakarta.persistence.EntityNotFoundException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
public class AnuncioService {
  
  @Autowired
  private AnuncioRepository anuncioRepository;

  @Autowired
  private UsuarioService usuarioService;

  public Anuncio createAnuncio(Anuncio anuncio) {
    if (!validateAnuncio(anuncio)) throw new IllegalArgumentException("Anúncio inválido");
    
    Usuario usuario = usuarioService.getUserById(anuncio.getUsuario().getId());

    if (usuario == null) {
      throw new EntityNotFoundException("Usuário não encontrado.");
    }

    Anuncio anuncioSalvo = anuncioRepository.save(anuncio);

    anuncioSalvo.setUsuario(usuario);

    return anuncioRepository.save(anuncioSalvo);
  }

  public Anuncio getAnuncioById(Long id) {
    return anuncioRepository.findById(id).orElseThrow(() -> new EntityNotFoundException("Anúncio com ID " + id + " não encontrado."));
  }

  public List<Anuncio> getAnuncioListByUsuario(Long userId) {
    Usuario usuario = usuarioService.getUserById(userId);
    if (usuario == null) {
      throw new EntityNotFoundException("Usuário com ID " + userId + " não encontrado.");
    }
    List<Anuncio> anuncios = anuncioRepository.findByUsuario(usuario);
    if (anuncios.isEmpty()) {
      throw new EntityNotFoundException("Nenhum anúncio encontrado para o usuário com ID " + userId + ".");
    } else {
      return anuncios;
    }
  }

  @Transactional
  public Anuncio updateAnuncio(Anuncio anuncio) {
    if (!validateAnuncio(anuncio)) throw new IllegalArgumentException("Anúncio inválido");
    
    Anuncio anuncioExistente = this.getAnuncioById(anuncio.getId());

    copiarDadosAnuncio(anuncioExistente, anuncio);

    return anuncioRepository.save(anuncioExistente);

  }

  private void copiarDadosAnuncio(Anuncio destino, Anuncio origem) {
    destino.setTitulo(origem.getTitulo());
    destino.setDescricao(origem.getDescricao());
    destino.setTags(origem.getTags());
    destino.setCidade(origem.getCidade());
    destino.setContratacoes(origem.getContratacoes());
    destino.setUsuario(origem.getUsuario());
  }

  public boolean validateAnuncio(Anuncio anuncio) {
    return anuncio != null &&
           anuncio.getTitulo() != null && !anuncio.getTitulo().isEmpty() &&
           anuncio.getDescricao() != null && !anuncio.getDescricao().isEmpty() &&
           anuncio.getTags() != null && !anuncio.getTags().isEmpty() &&
           anuncio.getCidade() != null && !anuncio.getCidade().isEmpty() &&
           anuncio.getUsuario() != null && anuncio.getUsuario().getId() != null;
  }

  @Transactional
  public void deleteAnuncio(Long id) {
    Anuncio anuncio = getAnuncioById(id);
    if (anuncio == null) {
      throw new EntityNotFoundException("Anúncio com ID " + id + " não encontrado.");
    }
    anuncioRepository.deleteById(id);
  }
}
