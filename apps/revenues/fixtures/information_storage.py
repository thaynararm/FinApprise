#Dados usados nos testes para validar se o formulário é valido quando recebe informações corretas

# ===========================================================
# ====================TESTE DAS CATEGORIAS===================
# ===========================================================

expected_data_for_test_correct_attributes_model_categories = {
    "category_name": "Receitas",
    "autor": "testuser",
}


# ===========================================================
# ==================TESTE DAS SUBCATEGORIAS==================
# ===========================================================

expected_data_for_test_correct_attributes_model_subcategories = {
    "category_name": "Receitas",
    "subcategory_name": "Receitas de Vendas",
    "autor": "testuser",
}



# ===========================================================
# =================TESTE DAS NOVAS RECEITAS==================
# ===========================================================

expected_data_for_test_correct_attributes_model_newrevenues ={
    "description": "Descrição da Receita",
    "date_of_competence": "2024-02-01",
    "subcategory": "Receitas de Serviços",
    "source": "Empresa ABC Ltda.",
    "value": 1876.90,
    "delivery_date": "2024-02-29",
    "receipt_account": "Conta Teste",
    "receipt_status": True,
    "comments": "Observação de teste",
    "autor": "testuser"
}
