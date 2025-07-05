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
        // TODO: Validações de regras de negócio??

        return admRepository.save(adm);
    }

    public Adm getAdmById(Long id) {
        return admRepository.findById(id)
                .orElseThrow(() -> new EntityNotFoundException("Usuário com ID " + id + " não encontrado."));
    }

    @Transactional
    public Adm updateAdm(Adm dadosDoRequest) {
        Adm admExistente = this.getAdmById(dadosDoRequest.getId());

        admExistente.setNome(dadosDoRequest.getNome());
        admExistente.setCargo(dadosDoRequest.getCargo());
        admExistente.setCpf(dadosDoRequest.getCpf());

        // TODO: Criptografar?
        if (dadosDoRequest.getSenha() != null && !dadosDoRequest.getSenha().isEmpty()) {
            admExistente.setSenha(dadosDoRequest.getSenha());
        }

        return admRepository.save(admExistente);
    }

    // TODO: validaAdm(Admin adm)

    @Transactional
    public void deleteAdm(Long id) {
        if (!admRepository.existsById(id)) {
            throw new EntityNotFoundException("Usuário não encontrado com o id: " + id);
        }
        admRepository.deleteById(id);
    }
}
