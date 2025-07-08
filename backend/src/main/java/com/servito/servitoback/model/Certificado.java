package com.servito.servitoback.model;

import jakarta.persistence.*;
import org.hibernate.annotations.CreationTimestamp;
import java.util.Date;

@Entity
@Table(name = "certificado")
public class Certificado {

  @Id
  @Column(nullable = false)
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  private Long id;
  
  @Column(nullable = false)
  private String titulo;
  
  @Column(nullable = false)
  private String instituicao;
  
  @CreationTimestamp
  @Temporal(TemporalType.TIMESTAMP)
  @Column(nullable = false)
  private Date data;
  
  private String link;
  
  private Boolean pendente = true;
  
  private Boolean aprovado = false;

  @ManyToOne
  @JoinColumn(name = "usuario_id", nullable = false)
  private Usuario usuario;

  public Certificado() {
  }

  public Certificado(Long id, String titulo, String instituicao, Date data) {
    this.id = id;
    this.titulo = titulo;
    this.instituicao = instituicao;
    this.data = data;
  }

  public Certificado(Long id, String titulo, String instituicao, Date data, String link) {
    this.id = id;
    this.titulo = titulo;
    this.instituicao = instituicao;
    this.data = data;
    this.link = link;
  }

  public Long getId() {
    return id;
  }

  public String getTitulo() {
    return titulo;
  }

  public String getInstituicao() {
    return instituicao;
  }

  public Date getData() {
    return data;
  }

  public String getLink() {
    return link;
  }

  public Boolean getPendente() {
    return pendente;
  }

  public Boolean getAprovado() {
    return aprovado;
  }

  public Usuario getUsuario() {
    return usuario;
  }

  public void setId(Long id) {
    this.id = id;
  }

  public void setTitulo(String titulo) {
    this.titulo = titulo;
  }

  public void setInstituicao(String instituicao) {
    this.instituicao = instituicao;
  }

  public void setData(Date data) {
    this.data = data;
  }

  public void setLink(String link) {
    this.link = link;
  }

  public void setPendente(Boolean pendente) {
    this.pendente = pendente;
  }

  public void setAprovado(Boolean aprovado) {
    this.aprovado = aprovado;
  }

  public void setUsuario(Usuario usuario) {
    this.usuario = usuario;
  }
}
