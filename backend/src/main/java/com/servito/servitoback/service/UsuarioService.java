package com.servito.servitoback.service;

import com.servito.servitoback.model.Historico;
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

    @Autowired
    private AdmService admService;

    @Autowired
    private HistoricoService historicoService;

    public List<Usuario> findAll() {
        return usuarioRepository.findAll();
    }

    @Transactional
    public Usuario createUsuario(Usuario usuario) {
        if (!validaUsuario(usuario)) throw new IllegalArgumentException("Usuário inválido");

        Usuario usuarioSalvo = usuarioRepository.save(usuario);
        Historico novoHistorico = historicoService.createHistorico(usuarioSalvo.getId());

        usuarioSalvo.setHistorico(novoHistorico);

        return usuarioRepository.save(usuarioSalvo);
    }

    public Usuario getUserById(Long id) {
        return usuarioRepository.findById(id)
                .orElseThrow(() -> new EntityNotFoundException("Usuário com ID " + id + " não encontrado."));
    }

    @Transactional
    public Usuario updateUsuario(Usuario usuario) {
        if (!validaUsuario(usuario)) throw new IllegalArgumentException("Usuário inválido");

        Usuario usuarioExistente = this.getUserById(usuario.getId());

        copiarDadosUsuario(usuarioExistente, usuario);

        return usuarioRepository.save(usuarioExistente);
    }

    private void copiarDadosUsuario(Usuario destino, Usuario origem) {
        destino.setNome(origem.getNome());
        destino.setEmail(origem.getEmail());
        destino.setSenha(origem.getSenha());
        destino.setTelefone(origem.getTelefone());
        destino.setDocumento(origem.getDocumento());
        destino.setEndereco(origem.getEndereco());
        destino.setCidade(origem.getCidade());
        destino.setDataNascimento(origem.getDataNascimento());
        destino.setBanned(origem.getBanned());
    }

    public boolean validaUsuario(Usuario usuario) {
        return usuario != null &&
                usuario.getNome() != null && !usuario.getNome().isBlank() &&
                usuario.getEmail() != null && !usuario.getEmail().isBlank() &&
                usuario.getSenha() != null && !usuario.getSenha().isBlank() &&
                usuario.getDocumento() != null && !usuario.getDocumento().isBlank() &&
                usuario.getDataCadastro() != null &&
                usuario.getDataNascimento() != null;
    }

    // TODO: createHistorico(Long userId) -> chamado na criação


    public Usuario setBanimento(Long idUsuario, Long idAdm) {
        if (this.admService.getAdmById(idAdm) == null) throw new IllegalArgumentException("Adm não encontrado");

        Usuario usuario = this.getUserById(idUsuario);
        usuario.setBanned(true);

        return usuarioRepository.save(usuario);

    }

    @Transactional
    public void deleteUsuario(Long id) {
        if (!usuarioRepository.existsById(id)) {
            throw new EntityNotFoundException("Usuário não encontrado com o id: " + id);
        }
        usuarioRepository.deleteById(id);
    }

}
