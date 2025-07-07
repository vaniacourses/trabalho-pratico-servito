package com.servito.servitoback.service;

import com.servito.servitoback.model.Historico;
import com.servito.servitoback.model.Historico;
import com.servito.servitoback.repository.HistoricoRepository;
import jakarta.persistence.EntityNotFoundException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
public class HistoricoService {

    @Autowired
    private HistoricoRepository historicoRepository;

    public List<Historico> findAll() {
        return historicoRepository.findAll();
    }

    @Transactional
    public Historico createHistorico(Long idUsuario) {
        return historicoRepository.save(new Historico(idUsuario));
    }

    public Historico getHistoricoById(Long id) {
        return historicoRepository.findById(id)
                .orElseThrow(() -> new EntityNotFoundException("Histórico com ID " + id + " não encontrado."));
    }

    @Transactional
    public Historico updateHistorico(Historico historico) {
        Historico historicoExistente = this.getHistoricoById(historico.getId());

        copiarDadosHistorico(historicoExistente, historico);

        return historicoRepository.save(historicoExistente);
    }

    private void copiarDadosHistorico(Historico destino, Historico origem) {
        destino.setComentario(origem.getComentario());
        destino.setNota(origem.getNota());
    }

    @Transactional
    public void deleteHistorico(Long id) {
        if (!historicoRepository.existsById(id)) {
            throw new EntityNotFoundException("Histórico não encontrado com o id: " + id);
        }
        historicoRepository.deleteById(id);
    }
}
