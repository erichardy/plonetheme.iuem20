
/*
 * Code jaavascript a ajouter dans un formulaire d'ajout/edition
 * d'element.
 * une piste : https://docs.plone.org/external/plone.app.dexterity/docs/advanced/custom-add-and-edit-forms.html#content-add-sequence
 * Il faut aussi déterminer comment composer la template qui va afficher le formulaire
 * standard, mais dans laquelle on va pouvoir ajouter le code javascript ci-dessous...?
 * car il n'est pas très "interressant" ni optimal d'ajouter ce code javascript pour
 * toutes les pages, pas exemple dans un theme...
 * voir : https://docs.plone.org/develop/plone/forms/z3c.form.html#rendering-a-form-manually
 * et : https://github.com/plone/plone.app.z3cform
 * et plus generalement : https://docs.plone.org/develop/plone/forms/z3c.form.html
 */
/*
 * Exemple de tableau required_fields
var required_fields = new Array();
required_fields = ['input#form-widgets-title',
	'input#form-widgets-title_en',
	'input#form-widgets-kw_fr',
	'input#form-widgets-kw_en',
	'input#form-widgets-supervisor_name1',
	'input#form-widgets-supervisor_email1',
	'select#form-widgets-discipline',
	'select#form-widgets-main_lab'
	];
On pourrait ameliorer la gestion des champs obligatoires en ajoutant la possibilite
d'un message adapte a chaque champ. Par exemple en creant un tableau des messages
correspondant a chaque champ.


 * les tableaux autotocs_objs et fieldsets_objs contiennent, dans le meme
 * ordre les relations entre les fiedsets et les autotocs.
 * Il suffit d'aller chercher l'index du fieldset et de retourner l'autotoc
 * du tableau autotocs_ids correspondant a cet index : cf fonction getAutotoc()
 */
autotocs_objs = $('#form nav a') ;
var autotocs_href = new Array();
for (i = 0 ; i < autotocs_objs.length ; i++){
	// contruction d'un tableau dont chaque element
	// contient le lien de chaque autotoc
	// 
	obj = autotocs_objs[i] ;
	obj_href = $(obj).attr('href');
	autotocs_href.push(obj_href);
	// console.log($(obj).attr("href"))
}

fieldsets_objs = $('#form fieldset');
var fieldsets_ids = new Array();
for (i = 0 ; i < fieldsets_objs.length ; i++){
	// contruction d'un tableau dont chaque element
	// contient l'ID de chaque fieldset.
	fieldset = fieldsets_objs[i];
	fieldsetId = $(fieldset).attr('id');
	fieldsets_ids.push(fieldsetId);
	// console.log($(fieldset).attr('id'));
}

/*
 * Fonction qui retourne le lien autotoc d'un fieldset
 */
function getAutotoc(fieldSetID) {
	// console.log(autotocs.length);
	for (i = 0 ; i < autotocs.length ; i++) {
		// console.log(i);
		// console.log(autotocs[i][0]);
		if (fieldsets_ids[i] == fieldSetID) {
			break;
		}
	}
	return autotocs[i];
}


// required_fields : liste des champs obligatoires
// cette liste est acquise par le panneau de conf
// la variable inputButton est aussi acquise par le panneau de conf.
inputButton = "input#form-buttons-save_this_thesis";
$(inputButton).click(function(e){
	for (i = 0 ; i < required_fields.length ; i++) {
		field = required_fields[i];
		val = $(field).val()
		if (val === ""){
			fieldsetId = $(field).parents("fieldset").attr('id');
			alert('Il manque des informations dans certains champs !');
			autotoc = getAutotoc(fieldsetId);
			$(autotoc).trigger("click");
			$(field).parent().css("color", "red");
			e.preventDefault();
			break;
		}
	}
});

