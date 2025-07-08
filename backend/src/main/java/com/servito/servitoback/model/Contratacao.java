package com.servito.servitoback.model;

import jakarta.persistence.*;

@Entity
@Table(name = "contratacao")
public class Contratacao {

  @Id
  @Column(nullable = false)
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  private Long id;

  @Column(nullable = false)
  private Integer preco;
  
  @Column(nullable = false)
  private String prazo;
  
  @Column(nullable = false)
  private String descricao;

  @Column(nullable = false)
  private Boolean aceita;
  
  @Column(nullable = false)
  private Boolean finalizada;
  
  @ManyToOne
  @JoinColumn(name = "prestador_id", nullable = false)
  private Usuario prestador;

  @ManyToOne
  @JoinColumn(name = "contratante_id", nullable = false)
  private Usuario contratante;

  @ManyToOne
  @JoinColumn(name = "anuncio_id", nullable = false)
  private Anuncio anuncio;

  public Contratacao() {
  }

  public Contratacao(Long id, Integer preco, String prazo, String descricao, Boolean aceita, Boolean finalizada, Usuario prestador, Usuario contratante, Anuncio anuncio) {
    this.id = id;
    this.preco = preco;
    this.prazo = prazo;
    this.descricao = descricao;
    this.aceita = aceita;
    this.finalizada = finalizada;
    this.prestador = prestador;
    this.contratante = contratante;
    this.anuncio = anuncio;
  }

  public Long getId() {
    return id;
  }

  public Integer getPreco() {
    return preco;
  }
  
  public String getPrazo() {
    return prazo;
  }

  public String getDescricao() {
    return descricao;
  }

  public Boolean getAceita() {
    return aceita;
  }

  public Boolean getFinalizada() {
    return finalizada;
  }

  public Usuario getPrestador() {
    return prestador;
  }

  public Usuario getContratante() {
    return contratante;
  }

  public Anuncio getAnuncio() {
    return anuncio;
  }

  public void setId(Long id) {
    this.id = id;
  }

  public void setPreco(Integer preco) {
    this.preco = preco;
  }

  public void setPrazo(String prazo) {
    this.prazo = prazo;
  }

  public void setDescricao(String descricao) {
    this.descricao = descricao;
  }

  public void setAceita(Boolean aceita) {
    this.aceita = aceita;
  }

  public void setFinalizada(Boolean finalizada) {
    this.finalizada = finalizada;
  }

  public void setPrestador(Usuario prestador) {
    this.prestador = prestador;
  }

  public void setContratante(Usuario contratante) {
    this.contratante = contratante;
  }

  public void setAnuncio(Anuncio anuncio) {
    this.anuncio = anuncio;
  }
}
