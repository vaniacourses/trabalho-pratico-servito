package com.servito.servitoback.repository;

import com.servito.servitoback.model.Contratacao;
import com.servito.servitoback.model.Usuario;
import com.servito.servitoback.model.Anuncio;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

public interface ContratacaoRepository extends JpaRepository<Contratacao, Long> {

  List<Contratacao> findByPrestador(Usuario prestador);
  List<Contratacao> findByContratante(Usuario contratante);
  List<Contratacao> findByAnuncio(Anuncio anuncio);
}
