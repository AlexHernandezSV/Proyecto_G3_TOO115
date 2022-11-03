$(document).ready(function(){
    
    var btnAddBenef = $('#add-benef');
    var totalForms = $('#id_form-TOTAL_FORMS').val();

    btnAddBenef.click(function(){
        if(totalForms<5){
        var formClone = $('#form-beneficiario-1').clone();

        formClone[0].id = 'form-beneficiario-'+(parseInt(totalForms)+1);
        formClone.appendTo('#forms-beneficiarios-container');

        //var inputParentesco= $('#form-beneficiario-6 #id_form-0-parentesco');
        var inputParentesco= formClone[0].querySelector('#id_form-0-parentesco');
        inputParentesco.id = 'id_form-'+totalForms+'-parentesco';
        inputParentesco.name = 'form-'+totalForms+'-parentesco';
        inputParentesco.value= '';

        var inputNombre= formClone[0].querySelector('#id_form-0-nombre');
        inputNombre.id = 'id_form-'+totalForms-+'nombre'
        inputNombre.name = 'form-'+totalForms+'-nombre'
        inputNombre.value= '';
        
        var inputApellido= formClone[0].querySelector('#id_form-0-apellido');
        inputApellido.id = 'id_form-'+totalForms+'-apellido'
        inputApellido.name = 'form-'+totalForms+'-apellido'
        inputApellido.value= '';
        
        var inputBeneficio= formClone[0].querySelector('#id_form-0-beneficio');
        inputBeneficio.id = 'id_form-'+totalForms+'-beneficio';
        inputBeneficio.name = 'form-'+totalForms+'-beneficio';
        inputBeneficio.value= 0.0000;

        var inputHidden= formClone[0].querySelector('#id_form-0-id');
        inputHidden.id = 'id_form-'+totalForms+'-id';
        inputHidden.name = 'form-'+totalForms+'-id';
        inputHidden.value= '';

        totalForms++;

        $('#id_form-TOTAL_FORMS').val(totalForms);

        var nBeneficiario = formClone[0].querySelector('#n-beneficiario');
        nBeneficiario.innerHTML = totalForms + ')';

        }
        if(totalForms>4){
            $(this).hide();
        };
    });


    var rdTrabajo = $('#empleo');
    var rdNegocio = $('#negocio');
    var rdAmbos = $('#negocio-empleo');
    var datosTrabajo = $('#datos-trabajo')
    var datosNegocio = $('#datos-negocio')
    datosTrabajo.hide();
    datosNegocio.hide();


    rdTrabajo.click(function(){
        datosNegocio.hide();
        datosNegocio.children().prop('disabled', true);
        datosTrabajo.show()
        datosTrabajo.children().prop('disabled', false);
    });
    rdNegocio.click(function(){
        datosNegocio.show();
        datosNegocio.children().prop('disabled', false);
        datosTrabajo.hide();
        datosTrabajo.children().prop('disabled', true);
    });
    rdAmbos.click(function(){
        datosNegocio.show();
        datosTrabajo.show();
        datosNegocio.children().prop('disabled', false);
        datosTrabajo.children().prop('disabled', false);
    });

    //Mapas

    let inputLat = document.getElementById("id_lat");
    let inputLng = document.getElementById("id_lng");
    let thisMarker;
    
    function initMap() {
      if(navigator.geolocation){

        navigator.geolocation.getCurrentPosition(
          (position) => {
            const pos = {
              lat: position.coords.latitude,
              lng: position.coords.longitude,
            };

            const map = new google.maps.Map(document.getElementById("map"), {
              zoom: 4,
              center: pos, //{ lat: -25.363882, lng: 131.044922 },
            });

            thisMarker = new google.maps.Marker({
              position: pos,//{lat:-25.363882, lng:131.044922},
              map: map,
              draggable: true,
          })
          /*inputLat.value = thisMarker.position.lat();
          inputLng.value = thisMarker.position.lng();
          */
         placeMarkerAndPanTo(pos,map)
          //Click event
          map.addListener("onmousedown", (e) => {
              placeMarkerAndPanTo(e.latLng, map);
            });

      })

      }else {
          // Browser doesn't support Geolocation
          pos = {
            lat: -25.363882,
            lng:131.044922,
          }
          const map = new google.maps.Map(document.getElementById("map"), {
            zoom: 4,
            center: pos, //{ lat: -25.363882, lng: 131.044922 },
          });

          thisMarker = new google.maps.Marker({
            position: pos,//{lat:-25.363882, lng:131.044922},
            map: map,
            draggable: true,
        })
        /*inputLat.value = thisMarker.position.lat();
        inputLng.value = thisMarker.position.lng();
        */
       placeMarkerAndPanTo(pos,map)
        //Click event
        map.addListener("onmousedown", (e) => {
            placeMarkerAndPanTo(e.latLng, map);
          });
        }

          function placeMarkerAndPanTo(latLng, map) {
            /*thisMarker = new google.maps.Marker({
               position: latLng,
               map: map,
               draggable: true,
             });*/
             map.panTo(latLng);
             inputLat.value = thisMarker.position.lat();
             inputLng.value = thisMarker.position.lng();
             
             google.maps.event.addListener(thisMarker,'position_changed',function(){
                 inputLat.value = thisMarker.position.lat();
                 inputLng.value = thisMarker.position.lng();
               });
           }


        
      }
      window.initMap = initMap();

});


