"use strict";

const gulp = require("gulp");

function py(done) {
  console.log("a")
  done();
}

// Watch files
function watchFiles() {
  gulp.watch("main.py", gulp.series(py));
}

const build = gulp.series(py);
const watch = gulp.parallel(watchFiles, build);

exports.build = build;
exports.watch = watch;
exports.default = watch;