"use strict";

const gulp = require("gulp");
const { spawn } = require('child_process');
var countPyRun = 0

function py(done) {
  countPyRun++;
  console.log("************************");
  console.log("Run %s:", countPyRun);
  console.log("************************");
  const pyProg = spawn('python', ['main.py']);
  pyProg.stdout.on('data', function(data) {
    console.log(data.toString());
  });
  done();
}

function watchFiles() {
  gulp.watch("main.py", gulp.series(py));
}

const build = gulp.series(py);
const watch = gulp.parallel(watchFiles, build);

exports.build = build;
exports.watch = watch;
exports.default = watch;