function validateCPF(cpf) {
    cpf = cpf.replace(/[^\d]+/g, '');
    if (cpf == '') return false;
    if (cpf.length != 11 ||
        cpf == "00000000000" ||
        cpf == "11111111111" ||
        cpf == "22222222222" ||
        cpf == "33333333333" ||
        cpf == "44444444444" ||
        cpf == "55555555555" ||
        cpf == "66666666666" ||
        cpf == "77777777777" ||
        cpf == "88888888888" ||
        cpf == "99999999999")
        return false;
    var add = 0;
    for (var i = 0; i < 9; i++)
        add += parseInt(cpf.charAt(i)) * (10 - i);
    var rev = 11 - (add % 11);
    if (rev == 10 || rev == 11)
        rev = 0;
    if (rev != parseInt(cpf.charAt(9)))
        return false;
    add = 0;
    for (var i = 0; i < 10; i++)
        add += parseInt(cpf.charAt(i)) * (11 - i);
    rev = 11 - (add % 11);
    if (rev == 10 || rev == 11)
        rev = 0;
    if (rev != parseInt(cpf.charAt(10)))
        return false;
    return true;
}

function validateForm() {
    var cpf = document.getElementById("cpf").value;
    var password = document.getElementById("password").value;
    var errorMessage = document.getElementById("error-message");

    if (!validateCPF(cpf)) {
        errorMessage.innerText = "CPF inválido!";
        return false;
    }

    if (password.length < 8) {
        errorMessage.innerText = "A senha deve ter pelo menos 8 caracteres!";
        return false;
    }

    // Clear the error message
    errorMessage.innerText = "";
    alert("Login bem-sucedido!"); // This is just a placeholder
    return true;
}

function redirectToRegister() {
    window.location.href = "cadastro.html";
}
function validateRegisterForm() {
    var nome = document.getElementById("nome").value;
    var cpf = document.getElementById("cpf").value;
    var password = document.getElementById("password").value;
    var errorMessage = document.getElementById("error-message");

    if (!validateCPF(cpf)) {
        errorMessage.innerText = "CPF inválido!";
        return false;
    }

    if (password.length < 8) {
        errorMessage.innerText = "A senha deve ter pelo menos 8 caracteres!";
        return false;
    }

    // Clear the error message
    errorMessage.innerText = "";
    alert("Cadastro bem-sucedido!"); // This is just a placeholder
    return true;
}