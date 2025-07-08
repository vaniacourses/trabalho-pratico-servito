package com.servito.servitoback.repository;

import com.servito.servitoback.model.Anuncio;
import com.servito.servitoback.model.Usuario;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

public interface AnuncioRepository extends JpaRepository<Anuncio, Long> {

    List<Anuncio> findByUsuario(Usuario usuario);
}
