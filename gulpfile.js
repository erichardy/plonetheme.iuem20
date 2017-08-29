var gulp = require('gulp');
var autoprefixer = require('gulp-autoprefixer');
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');
var debug = require('gulp-debug');
var fs = require('fs');
var shell = require('gulp-shell');

var concat = require('gulp-concat');
var notify = require('gulp-notify');
var cache = require('gulp-cache');
var notifier = require('node-notifier');

var rstfiles = ['docs/*.rst', './docs/*.py'];
var pyfiles = ['src/plonetheme/iuem20/*.py', 'src/plonetheme/iuem20/browser/*.py', 'src/plonetheme/iuem20/browser/behaviors/*.py', 'src/plonetheme/iuem20/browser/viewlets/*.py'];
var docfiles = rstfiles.concat(pyfiles)

var readme = 'README.rst';
w = process.cwd();

gulp.task('notifing', ['build-docs'], function() {
	notifier.notify({title: 'Sphinx',
			  message: 'build finished...'
	})
});

gulp.task('build-docs', shell.task('bin/sphinx-build docs docs/html', {cwd: '.'}))

gulp.task('readme', shell.task('cp README.rst docs', {cwd: '.'}))

gulp.task('docs', ['build-docs'], function() {
  gulp.watch(readme, ['readme'])
  gulp.watch(['./docs/*.rst', './docs/*.py', 'src/plonetheme/iuem20/*.py', 'src/plonetheme/iuem20/browser/*.py'], ['build-docs'])
})

gulp.task('htmldoc', ['build-docs'], function() {
  gulp.watch(readme, ['readme'])
  gulp.watch(['./docs/*.rst', './docs/*.py', 'src/plonetheme/iuem20/*.py', 'src/plonetheme/iuem20/browser/*.py'], ['build-docs'])
});


gulp.task('html', function() {
	// gulp.watch(['./docs/*.rst','src/plonetheme/iuem20/*.py', 'src/plonetheme/iuem20/browser/*.py'] , ['notifing'])
	gulp.watch(docfiles , ['notifing'])	
});

gulp.task('default', ['html']);


/* ***********  LESS  ********** */
/*
 * Pour construire les CSS a partir des fichiers LESS, utiliser :
 * # gulp less
 */
var lessfiles = ['src/plonetheme/iuem20/theme/less/*.less'];

gulp.task('build-css', shell.task('grunt compile', {cwd: '.'}))
gulp.task('notifingless', ['build-css'], function() {
	notifier.notify({title: 'LESS/CSS',
			  message: 'build finished...'
	})
});

gulp.task('less', function() {
	gulp.watch(lessfiles , ['notifingless'])	
});

/*

docs = gulp.task(
    'docs',
    function() {
        return gulp.src(docsfiles)
        .pipe(shell(['bin/sphinx-build -W docs docs/html']))
        .pipe(notify({message: 'Styles task complete'}))
    });

gulp.task('default', ['styles']);
gulp.task('watch', function() {
  gulp.watch(docsfiles, ['docs']);
});
*/
/* vim:set ft=javascript : */