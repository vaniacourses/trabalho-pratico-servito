package com.servito.servitoback.model;

import java.util.Date;

public interface Cadastro {

    String getNome();

    String getEmail();

    String getSenha();

    String getTelefone();

    String getDocumento();

    String getEndereco();

    String getCidade();

    Date getDataCadastro();

    void setNome(String nome);

    void setEmail(String email);

    void setSenha(String senha);

    void setTelefone(String telefone);

    void setDocumento(String documento);

    void setEndereco(String endereco);

    void setCidade(String cidade);

    void setDataCadastro(Date dataCadastro);

}