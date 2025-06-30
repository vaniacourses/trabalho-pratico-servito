package com.servito.servitoback.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Entity
@Table(name = "teste")
public class Teste {

  // Campos
  @Id
  @Column(nullable = false)
  private Long id;

  private String login;

  private String password;

  // Construtor vazio
  public Teste() {
  }

  // Construtor com campos
  public Teste(Long id, String login, String password) {
    this.id = id;
    this.login = login;
    this.password = password;
  }


  // Getters e Setters
  public String getLogin() {
    return login;
  }

  public void setLogin(String login) {
    this.login = login;
  }

  public String getPassword() {
    return password;
  }

  public void setPassword(String password) {
    this.password = password;
  }

  public Long getId() {
    return id;
  }

  public void setId(Long id) {
    this.id = id;
  }
}