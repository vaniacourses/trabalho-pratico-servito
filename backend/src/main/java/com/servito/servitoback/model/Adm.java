package com.servito.servitoback.model;

import jakarta.persistence.*;
import org.hibernate.annotations.CreationTimestamp;

import java.util.Date;


@Entity
@Table(name = "adm")
public class Adm implements Cadastro{

    @Id
    @Column(nullable = false)
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String cargo;

    private String nome;

    private String email;

    private String senha;

    private String telefone;

    private String documento;

    private String endereco;

    private String cidade;

    @CreationTimestamp
    @Temporal(TemporalType.TIMESTAMP)
    @Column(nullable = false, updatable = false)
    private Date dataCadastro;


    public Adm() {

    }

    public Adm(Long id, String cargo, String nome, String email, String senha, String telefone, String documento, String endereco, String cidade, Date dataCadastro) {
        this.id = id;
        this.cargo = cargo;
        this.nome = nome;
        this.email = email;
        this.senha = senha;
        this.telefone = telefone;
        this.documento = documento;
        this.endereco = endereco;
        this.cidade = cidade;
        this.dataCadastro = dataCadastro;
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

    public String getCargo() {
        return cargo;
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

    public void setCargo(String cargo) {
        this.cargo = cargo;
    }
}