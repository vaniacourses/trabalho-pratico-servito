package com.servito.servitoback.controller;

import com.servito.servitoback.model.Adm;
import com.servito.servitoback.service.AdmService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/admin")
public class AdmController {

    @Autowired
    private AdmService admService;

    @GetMapping
    public List<Adm> listarTodos() {
        return this.admService.findAll();
    }

    @PostMapping
    public Adm createAdmin(@RequestBody Adm adm) {
        return this.admService.createAdm(adm);
    }

    @GetMapping("/{id}")
    public Adm getAdmById(@PathVariable Long id) {
        return this.admService.getAdmById(id);
    }

    @PutMapping
    public Adm updateAdm(@RequestBody Adm adm) {
        return this.admService.updateAdm(adm);
    }

    @DeleteMapping("/{id}")
    public void deleteAdmin(@PathVariable Long id) {
        this.admService.deleteAdm(id);
    }

    // TODO: validaAdm(Admin adm)

}
