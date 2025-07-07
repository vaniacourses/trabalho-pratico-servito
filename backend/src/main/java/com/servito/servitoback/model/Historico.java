package com.servito.servitoback.model;

import jakarta.persistence.*;

@Entity
public class Historico {
  @Id
  @Column(nullable = false)
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  private Long id;

  private String comentario;

  @Column(nullable = false)
  private Integer nota;

  public Historico() {
  }

  public Historico(Long id) {
    this.id = id;
    this.comentario = null;
    this.nota = null;
  }

  public Historico(Long id, String comentario, Integer nota) {
    this.id = id;
    this.comentario = comentario;
    this.nota = nota;
  }

  public Long getId() {
    return id;
  }

  public void setId(Long id) {
    this.id = id;
  }

  public String getComentario() {
    return comentario;
  }

  public void setComentario(String comentario) {
    this.comentario = comentario;
  }

  public Integer getNota() {
    return nota;
  }

  public void setNota(Integer nota) {
    this.nota = nota;
  }
}