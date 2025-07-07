package com.servito.servitoback.controller;

import com.servito.servitoback.model.Historico;
import com.servito.servitoback.service.HistoricoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/historico")
public class HistoricoController {

    @Autowired
    private HistoricoService historicoService;

    @GetMapping
    public List<Historico> listarTodos() {
        return this.historicoService.findAll();
    }

    @GetMapping("/{id}")
    public Historico getHistoricoById(@PathVariable Long id) {
        return this.historicoService.getHistoricoById(id);
    }

    @PutMapping
    public Historico updateHistorico(@RequestBody Historico historico) {
        return this.historicoService.updateHistorico(historico);
    }

    @DeleteMapping("/{id}")
    public void deleteHistorico(@PathVariable Long id) {
        this.historicoService.deleteHistorico(id);
    }


}
