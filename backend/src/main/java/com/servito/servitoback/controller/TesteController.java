package com.servito.servitoback.controller;

import com.servito.servitoback.model.Teste;
import com.servito.servitoback.service.TesteService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;

import java.util.List;

@RestController
@RequestMapping("/teste")
class TesteController {

    @Autowired
    private TesteService testeService;

    @GetMapping
    public List<Teste> listarTodos() {
        return testeService.findAll();
    }
}
