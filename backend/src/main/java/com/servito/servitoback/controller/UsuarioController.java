package com.servito.servitoback.controller;

import com.servito.servitoback.model.Usuario;
import com.servito.servitoback.service.UsuarioService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/usuario")
public class UsuarioController {

    @Autowired
    private UsuarioService usuarioService;

    @GetMapping
    public List<Usuario> listarTodos() {
        return this.usuarioService.findAll();
    }

    @PostMapping
    public Usuario createUsuario(@RequestBody Usuario usuario) {
        return this.usuarioService.createUsuario(usuario);
    }

    @GetMapping("/{id}")
    public Usuario getUserById(@PathVariable Long id) {
        return this.usuarioService.getUserById(id);
    }

    @PutMapping
    public Usuario updateUsuario(@RequestBody Usuario usuario) {
        return this.usuarioService.updateUsuario(usuario);
    }

    @DeleteMapping("/{id}")
    public void deleteUsuario(@PathVariable Long id) {
        this.usuarioService.deleteUsuario(id);
    }

    @PutMapping("/adm/{idAdm}/banir/{idUsuario}")
    public Usuario setBanimento(@PathVariable Long idAdm, @PathVariable Long idUsuario) {
        return this.usuarioService.setBanimento(idAdm, idUsuario);
    }


    }
