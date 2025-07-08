package com.servito.servitoback.controller;

import com.servito.servitoback.model.Contratacao;
import com.servito.servitoback.service.ContratacaoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/contratacao")
public class ContratacaoController {
  
  @Autowired
  private ContratacaoService contratacaoService;

  @PostMapping
  public Contratacao createContratacao(@RequestBody Contratacao contratacao) {
    return this.contratacaoService.createContratacao(contratacao);
  }

  @GetMapping("/{id}")
  public Contratacao getContratacaoById(@PathVariable Long id) {
    return this.contratacaoService.getContratacaoById(id);
  }

  @PutMapping
  public Contratacao updateContratacao(@RequestBody Contratacao contratacao) {
    return this.contratacaoService.updateContratacao(contratacao);
  }

  @DeleteMapping("/{id}")
  public void deleteContratacao(@PathVariable Long id) {
    this.contratacaoService.deleteContratacao(id);
  }

  @GetMapping("/prestador/{userId}")
  public List<Contratacao> getContratacaoListByPrestador(@RequestBody Long userId) {
    return this.contratacaoService.getContratacaoListByPrestador(userId);
  }

  @GetMapping("/contratante/{userId}")
  public List<Contratacao> getContratacaoListByContratante(@RequestBody Long userId) {
    return this.contratacaoService.getContratacaoListByContratante(userId);
  }

  @GetMapping("/anuncio/{anuncioId}")
  public List<Contratacao> getContratacaoListByAnuncio(@RequestBody Long anuncioId) {
    return this.contratacaoService.getContratacaoListByAnuncio(anuncioId);
  }

}
