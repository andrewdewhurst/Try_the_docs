# ------------ Custom settings --------------
$title = "XVF3610 USer Guide"
$version = "5.0.0"
$keep_versions = "4.0.0"

# -------------------------------------------



#Uses env variables to pass this info tot he conf.py file
$env:DOC_TITLE = $title
$env:DOC_VERSION = $version

#removes old content if this desitination folder (i.e. named with this version) alreayd exists
if (test-Path ./_html/$version) {
    write-Output "Removing old content in output directory: $version"
    remove-Item ./_html/$version/* -Include *.* -Recurse
}

#creates the html template which provides the version drop-down
python versioning.py -v $keep_versions


#run doxygen
#
# STILL TODO


#runs sphinx
sphinx-build -c . .. ./_html/$version

#copies the new version to "latest" as this allows old versions always to navigate to the newest one
if (test-Path ./_html/latest) {
    write-Output "Replace latest content with a copy of $version"
    remove-Item ./_html/latest -Recurse
}

copy-Item  -Path ./_html/$version/  -Destination ./_html/latest/ -Recurse
