package com.servito.servitoback.service;

import com.servito.servitoback.model.Usuario;
import com.servito.servitoback.repository.UsuarioRepository;
import jakarta.persistence.EntityNotFoundException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
public class UsuarioService {

    @Autowired
    private UsuarioRepository usuarioRepository;

    public List<Usuario> findAll() {
        return usuarioRepository.findAll();
    }

    @Transactional
    public Usuario createUsuario(Usuario usuario) {
        // TODO: Validações de regras de negócio??

        return usuarioRepository.save(usuario);
    }

    public Usuario getUserById(Long id) {
        return usuarioRepository.findById(id)
                .orElseThrow(() -> new EntityNotFoundException("Usuário com ID " + id + " não encontrado."));
    }

    @Transactional
    public Usuario updateUsuario(Usuario dadosDoRequest) {
        Usuario usuarioExistente = this.getUserById(dadosDoRequest.getId());

        usuarioExistente.setEmail(dadosDoRequest.getEmail());
        usuarioExistente.setNome(dadosDoRequest.getNome());
        usuarioExistente.setDataNascimento(dadosDoRequest.getDataNascimento());
        usuarioExistente.setDataCadastro(dadosDoRequest.getDataCadastro());
        usuarioExistente.setCpf(dadosDoRequest.getCpf());

        // TODO: Criptografar?
        if (dadosDoRequest.getSenha() != null && !dadosDoRequest.getSenha().isEmpty()) {
            usuarioExistente.setSenha(dadosDoRequest.getSenha());
        }

        return usuarioRepository.save(usuarioExistente);
    }

    // TODO: validaUsuario(Usuario usuario)

    // TODO: setBanimento(Long idAdm)

    @Transactional
    public void deleteUsuario(Long id) {
        if (!usuarioRepository.existsById(id)) {
            throw new EntityNotFoundException("Usuário não encontrado com o id: " + id);
        }
        usuarioRepository.deleteById(id);
    }

}
