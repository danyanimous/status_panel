(async () => {
    const text = await (await fetch("status.txt")).text();
	setTimeout(() => {
		document.getElementById("text").innerHTML = text; 
	}, 8);
})();

