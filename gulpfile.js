"use strict";

const gulp = require("gulp");
const { spawn } = require('child_process');
const exec = require('child_process').exec;

var countPyRun = 0

function py(done) {
  countPyRun++;
  console.log("************************");
  console.log("Run %s:", countPyRun);
  console.log("************************");
  /*
  const pyProg = spawn('python', ['main.py', 'a']);
  pyProg.stdout.on('data', function(data) {
    console.log(data.toString());
  });
  */
  exec('python3 main.py < input', function(err, stdout, stderr) {
    if (err) {
      return console.error('exec error:', err);
    }
    console.log(stdout);
    if (stderr){
      console.log("stderr");
      console.log(stderr);
    }
  });
  done();
}

function watchFiles() {
  gulp.watch(["main.py", "input"], gulp.series(py));
}

const build = gulp.series(py);
const watch = gulp.parallel(watchFiles, build);

exports.build = build;
exports.watch = watch;
exports.default = watch;