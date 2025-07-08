package com.servito.servitoback.controller;

import com.servito.servitoback.model.Anuncio;
import com.servito.servitoback.service.AnuncioService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/anuncio")
public class AnuncioController {
  
  @Autowired
  private AnuncioService anuncioService;

  @PostMapping
  public Anuncio createAnuncio(@RequestBody Anuncio anuncio) {
    return this.anuncioService.createAnuncio(anuncio);
  }

  @GetMapping("/{id}")
  public Anuncio getAnuncioById(@PathVariable Long id) {
    return this.anuncioService.getAnuncioById(id);
  }

  @PutMapping
  public Anuncio updateAnuncio(@RequestBody Anuncio anuncio) {
    return this.anuncioService.updateAnuncio(anuncio);
  }

  @DeleteMapping("/{id}")
  public void deleteAnuncio(@PathVariable Long id) {
    this.anuncioService.deleteAnuncio(id);
  }

  @GetMapping("/usuario/{userId}")
  public List<Anuncio> getAnuncioListByUsuario(@RequestBody Long userId) {
    return this.anuncioService.getAnuncioListByUsuario(userId);
  }

}
