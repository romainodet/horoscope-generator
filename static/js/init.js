function horoscope() {
    console.log("okfunc")
    $(function () {
        $.getJSON("http://127.0.0.1:5000/_horoscope",
            function (data) {

                $("#belier").text(data.belier);
                $("#taureau").text(data.taureau);
                $("#gemeaux").text(data.gemeaux);
                $("#cancer").text(data.cancer);
                $("#lion").text(data.lion);
                $("#vierge").text(data.vierge);
                $("#balance").text(data.balance);
                $("#scorpion").text(data.scorpion);
                $("#sagittaire").text(data.sagittaire);
                $("#capricorne").text(data.capricorne);
                $("#verseau").text(data.verseau);
                $("#poisson").text(data.poissons);

                console.log("Refresh Horoscope")
            });
    });
}

window.onload = horoscope();

console.log("ok")