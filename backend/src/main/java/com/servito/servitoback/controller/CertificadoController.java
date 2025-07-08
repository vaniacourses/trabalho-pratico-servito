package com.servito.servitoback.controller;

import com.servito.servitoback.model.Certificado;
import com.servito.servitoback.service.CertificadoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/certificado")
public class CertificadoController {
  
  @Autowired
  private CertificadoService certificadoService;

  @PostMapping
  public Certificado createCertificado(@RequestBody Certificado certificado) {
    return this.certificadoService.createCertificado(certificado);
  }

  @GetMapping("/{id}")
  public Certificado getCertificadoById(@PathVariable Long id) {
    return this.certificadoService.getCertificadoById(id);
  }

  @PutMapping
  public Certificado updateCertificado(@RequestBody Certificado certificado) {
    return this.certificadoService.updateCertificado(certificado);
  }

  @DeleteMapping("/{id}")
  public void deleteCertificado(@PathVariable Long id) {
    this.certificadoService.deleteCertificado(id);
  }

  @GetMapping("/usuario/{userId}")
  public List<Certificado> getCertificadoListByUserId(@PathVariable Long userId) {
    return this.certificadoService.getCertificadoListByUserId(userId);
  }

  @GetMapping("/pendente")
  public List<Certificado> getCertificadosPendentes() {
    return this.certificadoService.getCertificadosPendentes();
  }

}
