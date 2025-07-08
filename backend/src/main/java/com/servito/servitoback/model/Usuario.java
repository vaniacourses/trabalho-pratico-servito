package com.servito.servitoback.model;

import jakarta.persistence.*;
import org.hibernate.annotations.CreationTimestamp;

import java.util.Date;
import java.util.List;

@Entity
@Table(name = "usuario")
public class Usuario implements Cadastro{

  @Id
  @Column(nullable = false)
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  private Long id;

  @Column(nullable = false)
  private String nome;

  @Column(nullable = false)
  private String email;

  @Column(nullable = false)
  private String senha;

  private String telefone;

  @Column(nullable = false)
  private String documento;

  private String endereco;

  private String cidade;

  @CreationTimestamp
  @Temporal(TemporalType.TIMESTAMP)
  @Column(nullable = false, updatable = false)
  private Date dataCadastro;

  @Column(nullable = false)
  private Date dataNascimento;

  private Boolean isBanned = false;

  @OneToMany(mappedBy = "usuario", cascade = CascadeType.ALL)
  private List<Anuncio> anuncios;

//  @OneToOne(cascade = CascadeType.ALL, orphanRemoval = true)
//  @JoinColumn(name = "historico_id", referencedColumnName = "id")
//  private Historico historico;

  @OneToMany(mappedBy = "usuario", cascade = CascadeType.ALL)
  private List<Certificado> certificados;

  public Usuario() {
  }

  public Usuario(Long id, String nome, String email, String senha, String telefone, String documento, String endereco, String cidade, Date dataCadastro, Date dataNascimento, Boolean isBanned, List<Anuncio> anuncios, List<Certificado> certificados) {
    this.id = id;
    this.nome = nome;
    this.email = email;
    this.senha = senha;
    this.telefone = telefone;
    this.documento = documento;
    this.endereco = endereco;
    this.cidade = cidade;
    this.dataCadastro = dataCadastro;
    this.dataNascimento = dataNascimento;
    this.isBanned = isBanned;
    this.anuncios = anuncios;
    this.certificados = certificados;
  }

  @Override
  public String getNome() {
    return nome;
  }

  @Override
  public String getEmail() {
    return email;
  }

  @Override
  public String getSenha() {
    return senha;
  }

  @Override
  public String getTelefone() {
    return telefone;
  }

  @Override
  public String getDocumento() {
    return documento;
  }

  @Override
  public String getEndereco() {
    return endereco;
  }

  @Override
  public String getCidade() {
    return cidade;
  }

  @Override
  public Date getDataCadastro() {
    return dataCadastro;
  }

  public Long getId() {
    return id;
  }

  public Date getDataNascimento() {
    return dataNascimento;
  }

  public Boolean getBanned() {
    return isBanned;
  }

  @Override
  public void setNome(String nome) {
    this.nome = nome;
  }

  @Override
  public void setEmail(String email) {
    this.email = email;
  }

  @Override
  public void setSenha(String senha) {
    this.senha = senha;
  }

  @Override
  public void setTelefone(String telefone) {
    this.telefone = telefone;
  }

  @Override
  public void setDocumento(String documento) {
    this.documento = documento;
  }

  @Override
  public void setEndereco(String endereco) {
    this.endereco = endereco;
  }

  @Override
  public void setCidade(String cidade) {
    this.cidade = cidade;
  }

  @Override
  public void setDataCadastro(Date dataCadastro) {
    this.dataCadastro = dataCadastro;
  }

  public void setDataNascimento(Date dataNascimento) {
    this.dataNascimento = dataNascimento;
  }

  public void setBanned(Boolean banned) {
    this.isBanned = banned;
  }

  public void setId(Long id) {
    this.id = id;
  }

  public List<Anuncio> getAnuncios() {
    return anuncios;
  }

  public void setAnuncios(List<Anuncio> anuncios) {
    this.anuncios = anuncios;
  }

  public List<Certificado> getCertificados() {
    return certificados;
  }

  public void setCertificados(List<Certificado> certificados) {
    this.certificados = certificados;
  }

  //  public Historico getHistorico() {
//    return historico;
//  }
//
//  public void setHistorico(Historico historico) {
//    this.historico = historico;
//  }
}

