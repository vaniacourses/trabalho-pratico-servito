package com.servito.servitoback.model;

import jakarta.persistence.*;

import java.util.Date;

@Entity
@Table(name = "usuario")
public class Usuario {

  @Id
  @Column(nullable = false)
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  private Long id;

  private String email;

  private String senha;

  private String nome;

  private Date dataNascimento;

  private Date dataCadastro;

  private String cpf;

  private Boolean isBanned;

  public Usuario() {
    super();
  }

  public Usuario(Long id, String email, String senha, String nome, Date dataNascimento, Date dataCadastro, String cpf) {
    this.id = id;
    this.email = email;
    this.senha = senha;
    this.nome = nome;
    this.dataNascimento = dataNascimento;
    this.dataCadastro = dataCadastro;
    this.cpf = cpf;
    this.isBanned = false;
  }

  public Long getId() {
    return id;
  }

  public void setId(Long id) {
    this.id = id;
  }

  public String getEmail() {
    return email;
  }

  public void setEmail(String email) {
    this.email = email;
  }

  public String getSenha() {
    return senha;
  }

  public void setSenha(String senha) {
    this.senha = senha;
  }

  public String getNome() {
    return nome;
  }

  public void setNome(String nome) {
    this.nome = nome;
  }

  public Date getDataNascimento() {
    return dataNascimento;
  }

  public void setDataNascimento(Date dataNascimento) {
    this.dataNascimento = dataNascimento;
  }

  public Date getDataCadastro() {
    return dataCadastro;
  }

  public void setDataCadastro(Date dataCadastro) {
    this.dataCadastro = dataCadastro;
  }

  public String getCpf() {
    return cpf;
  }

  public void setCpf(String cpf) {
    this.cpf = cpf;
  }

  public Boolean getBanned() {
    return isBanned;
  }

  public void setBanned(Boolean banned) {
    isBanned = banned;
  }
}

