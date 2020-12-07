function signUp(){
    window.open("{{ url_for('signup14G')}}");
    window.close();
    return 
}
function buscar(){
    // window.open({{ url_for('signup14G')}});
    // window.close();
    a='{{ url_for("signup14G")}}'
    return a
}