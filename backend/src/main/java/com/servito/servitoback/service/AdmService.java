package com.servito.servitoback.service;

import com.servito.servitoback.model.Adm;
import com.servito.servitoback.repository.AdmRepository;
import jakarta.persistence.EntityNotFoundException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
public class AdmService {

    @Autowired
    private AdmRepository admRepository;

    public List<Adm> findAll() {
        return admRepository.findAll();
    }

    @Transactional
    public Adm createAdm(Adm adm) {
        if (!validaAdm(adm)) throw new IllegalArgumentException("Adm inválido");

        return admRepository.save(adm);
    }

    public Adm getAdmById(Long id) {
        return admRepository.findById(id)
                .orElseThrow(() -> new EntityNotFoundException("Usuário com ID " + id + " não encontrado."));
    }

    @Transactional
    public Adm updateAdm(Adm adm) {
        if (!validaAdm(adm)) throw new IllegalArgumentException("Adm inválido");

        Adm admExistente = this.getAdmById(adm.getId());

        copiarDadosAdm(admExistente, adm);

        return admRepository.save(admExistente);
    }

    private void copiarDadosAdm(Adm destino, Adm origem) {
        destino.setNome(origem.getNome());
        destino.setEmail(origem.getEmail());
        destino.setSenha(origem.getSenha());
        destino.setTelefone(origem.getTelefone());
        destino.setEndereco(origem.getEndereco());
        destino.setCidade(origem.getCidade());
        destino.setDocumento(origem.getDocumento());
        destino.setCargo(origem.getCargo());
    }

    public boolean validaAdm(Adm adm) {
        return adm != null &&
                adm.getNome() != null && !adm.getNome().isBlank() &&
                adm.getEmail() != null && !adm.getEmail().isBlank() &&
                adm.getSenha() != null && !adm.getSenha().isBlank() &&
                adm.getDocumento() != null && !adm.getDocumento().isBlank() &&
                adm.getDataCadastro() != null &&
                adm.getCargo() != null  && !adm.getCargo().isBlank();
    }


    @Transactional
    public void deleteAdm(Long id) {
        if (!admRepository.existsById(id)) {
            throw new EntityNotFoundException("Usuário não encontrado com o id: " + id);
        }
        admRepository.deleteById(id);
    }
}
