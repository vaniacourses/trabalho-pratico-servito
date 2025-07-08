package com.servito.servitoback.model;

import java.util.List;
import jakarta.persistence.*;

@Entity
@Table(name = "anuncio")
public class Anuncio {
  @Id
  @Column(nullable = false)
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  private Long id;

  @Column(nullable = false)
  private String titulo;

  @Column(nullable = false)
  private String descricao;
  
  @ElementCollection
  private List<String> tags;
  
  @Column(nullable = false)
  private String cidade;

  @OneToMany(mappedBy = "anuncio", cascade = CascadeType.ALL)
  private List<Contratacao> contratacoes;

  @ManyToOne
  @JoinColumn(name = "usuario_id", nullable = false)
  private Usuario usuario;

  public Anuncio() {
  }

  public Anuncio(Long id, String titulo, String descricao, List<String> tags, String cidade, List<Contratacao> contratacoes, Usuario usuario) {
    this.id = id;
    this.titulo = titulo;
    this.descricao = descricao;
    this.tags = tags;
    this.cidade = cidade;
    this.contratacoes = contratacoes;
    this.usuario = usuario;
  }

  public Long getId() {
    return id;
  }

  public String getTitulo() {
    return titulo;
  }

  public String getDescricao() {
    return descricao;
  }

  public List<String> getTags() {
    return tags;
  }
  
  public String getCidade() {
    return cidade;
  }
  
  public List<Contratacao> getContratacoes() {
    return contratacoes;
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

  public void setDescricao(String descricao) {
    this.descricao = descricao;
  }

  public void setTags(List<String> tags) {
    this.tags = tags;
  }

  public void setCidade(String cidade) {
    this.cidade = cidade;
  }

  public void setContratacoes(List<Contratacao> contratacoes) {
    this.contratacoes = contratacoes;
  }

  public void setUsuario(Usuario usuario) {
    this.usuario = usuario;
  }
  
}
