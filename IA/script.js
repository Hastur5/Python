function showDetails(eventId) {
    const eventDetail = document.getElementById(eventId);
    if (eventDetail.style.display === "none" || eventDetail.style.display === "") {
        eventDetail.style.display = "block";
    } else {
        eventDetail.style.display = "none";
    }
}