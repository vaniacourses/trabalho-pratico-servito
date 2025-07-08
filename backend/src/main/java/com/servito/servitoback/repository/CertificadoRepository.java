package com.servito.servitoback.repository;

import com.servito.servitoback.model.Certificado;
import com.servito.servitoback.model.Usuario;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

public interface CertificadoRepository extends JpaRepository<Certificado, Long> {

    List<Certificado> findByUsuario(Usuario usuario);
}