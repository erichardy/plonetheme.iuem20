/* Copie de bebest-theme.js */
/* essai de correction du bug d'affichage quand on saisi les contacts
 * et que l'on clique sur l'icone pour avoir l'arborescence
 * 
 * Sans succes !!!
$('.glyphicon-indent-left').click(function(){
	$('.pattern-relateditems-path').each(function(){
		console.log($(this));
		$(this).removeProp('z-index');
	});
});

$('.pattern-relateditems-tree').click(function(){
	// console.log($(this).parent());
	parent = $(this).parent();
	$(parent).css('padding-bottom', '100px');
})
*/

/*
 * Dans les formulaires d'ajout/modif des elements, permet que l'URL
 * vers geojson.io soit cliquable
 */
geojson_help = 'Utiliser / Use : <a href="http://geojson.io/" target="_blank">http://geojson.io/</a>';
$('#formfield-form-widgets-geojson span.formHelp').html(geojson_help);

/* sous-menus de la nav bar */
/* code from http://codepen.io/betdream/pen/frDqh */
/*
 * Permet de montrer/cacher (sans clic, par hover) un sous-menu de la nav-bar
 */
$('ul.nav li.dropdown').hover(function() {
  $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeIn(500);
}, function() {
  $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeOut(500);
});

// pour que la description du dossier n'apparaisse pas dans le sous-menu
$("span.submenu_description").css("display", "none");

/* FIN sous-menus de la nav bar */


/*
 * Dans la section "about", fait apparaitre l'image de decoration
 * a droite quand le scroll de la page arrive sur cette section
 */
$(window).scroll(function() {
	$('#scrollreveal').each(function(){
		var imagePos = $(this).offset().top;
		var topOfWindow = $(window).scrollTop();
			if (imagePos < topOfWindow + 500) {
				$(this).addClass("fadeIn");
			}		
		});
});

bodyClasses = document.getElementById("visual-portal-wrapper").classList ;


/* Les boutons d'affichage/cache des versions anglaises */
/*
 * - un bouton est de la classe "collapser"
 * - son id est, par exemple : show-english-version
 * - le clic sur ce bouton montre/cache un element du DOM qui
 *   a pour id : show-english-version-collapse
 */
$("button.collapser").click(function(e){
	to_show = $(this).attr("id") + '-collapse';
	$("#" + to_show).toggle("slow", "swing", function(e){
		display = $("#" + to_show).css("display");
		if (display === "block"){
			$("#" + to_show).css("display", "flex");
		}
	});
})
/* FIN Les boutons d'affichage/cache des versions anglaises */


/*
 * Gestion des mails
 */
$("a#person-contact").on('click',function(e){
	var mail = $('#person-contact-coded').attr('contact');
	eemail = decryptEmail(mail);
	$(this).attr('href', "mailto:" + decryptEmail(mail ));
})	

function decryptEmail(encodedEmail){
	// S'IL NE FAUT PAS DECODER LA CHAINE DE CARACTERES OU SI ELLE EST VIDE.....
	if(( encodedEmail == undefined )
	||( encodedEmail.indexOf("__") == -1)
	||( encodedEmail	== "on__liam" )
	||( encodedEmail =="")) {
		return false;
	}
	// SEPARATION DU NOM ET DU HOST DANS UN TABLEAU ..........................
	var partsTabs	= encodedEmail.split("__");

	var encodedFirstWords	= partsTabs[0].split("_");
	var encodedLastWords	= partsTabs[1].split("_");
	// RECONSTRUCTION DU DEBUT ................................................ 
	var firstWords	= reconstructWord( encodedFirstWords );
	// RECONSTRUCTION DE LA FIN ...............................................
	var lastWords	= reconstructWord( encodedLastWords );
	return firstWords + "@" + lastWords ;
}

function reconstructWord(wordsToReconstruct){
	var wordDecoded	= "";
	// ON CONCATENE TOUTES LES PARTIES SAUF LA DERNIERE..................................
	for( i=0 ; i < wordsToReconstruct.length -1; i++) {
		wordDecoded	= wordDecoded + inverseLetters( wordsToReconstruct[i] ) + ".";	
	}
	// ON AJOUTE LA DERNIERE PARTIE .....................................................
	wordDecoded	= wordDecoded + inverseLetters(wordsToReconstruct[wordsToReconstruct.length -1]);
	return wordDecoded;
}

function inverseLetters(encodedInverseEmail){
	if ( encodedInverseEmail == "") return "";
	var encodedEmail = "";
	for(var i= encodedInverseEmail.length-1; i>=0 ; i-- ){
		encodedEmail += encodedInverseEmail[i];
	}
	return encodedEmail.replace("_", ".");
}
/* FIN Gestion des mails */
