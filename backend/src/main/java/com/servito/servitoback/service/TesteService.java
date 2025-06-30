package com.servito.servitoback.service;

import com.servito.servitoback.model.Teste;
import com.servito.servitoback.repository.TesteRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class TesteService {

    @Autowired
    private TesteRepository testeRepository;

    public List<Teste> findAll() {
        return testeRepository.findAll();
    }

    public Optional<Teste> findById(Long id) {
        return testeRepository.findById(id);
    }

    public Teste save(Teste produto) {
        return testeRepository.save(produto);
    }

    public void deleteById(Long id) {
        testeRepository.deleteById(id);
    }

    public Teste update(Long id, Teste testeAtualizado) {
        return testeRepository.findById(id)
                .map(testeExistente -> {
                    testeExistente.setLogin(testeAtualizado.getLogin());
                    testeExistente.setPassword(testeAtualizado.getPassword());
                    return testeRepository.save(testeExistente);
                }).orElseThrow(() -> new RuntimeException("Teste não encontrado com id " + id));
    }
}
