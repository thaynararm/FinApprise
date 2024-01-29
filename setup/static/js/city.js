const urlUf = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados';
const city = $('#city');
const uf = $('#uf');

// Inicialize o Select2 para os elementos uf e city
uf.select2();
city.select2();

uf.on('change', async function() {
    let urlCities;
    if(uf.val() == 'DF') {
    urlCities = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/' + uf.val() + '/subdistritos';
    } else {
    urlCities = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/' + uf.val() + '/municipios';
    }

    const request = await fetch(urlCities);
    const response = await request.json();

    response.sort((a, b) => a.nome.localeCompare(b.nome));

    let options = '<option>Selecione a cidade</option>'; // Adicione uma opção vazia para desmarcar a cidade

    response.forEach(function(city) {
    options += '<option value="' + city.nome + '">' + city.nome + '</option>';
    });

    city.html(options);
    // Atualize o Select2 após alterar as opções
    city.trigger('change');
});

$(document).ready(async function() {
    const request = await fetch(urlUf);
    const response = await request.json();

    response.sort((a, b) => a.nome.localeCompare(b.nome));

    let options = '<option>Selecione o estado</option>'; // Adicione uma opção vazia para desmarcar o estado

    response.forEach(function(uf) {
    options += '<option value="' + uf.sigla + '">' + uf.sigla + '</option>';
    });

    uf.html(options);
    // Atualize o Select2 após alterar as opções
    uf.trigger('change');
});