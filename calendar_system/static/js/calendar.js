let calendar;

document.addEventListener("DOMContentLoaded", function () {
  const calendarEl = document.getElementById("calendar");

  calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: "dayGridMonth",
    editable: true,
    events: "/api/events",

    eventDrop: function (info) {
      fetch("/api/update-event", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          id: info.event.id,
          start: info.event.start.toISOString(),
          end: info.event.end
            ? info.event.end.toISOString()
            : info.event.start.toISOString()
        })
      });
    }
  });

  calendar.render();
});


function addEvent() {
  fetch("/api/add-event", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      title: document.getElementById("title").value,
      start: document.getElementById("start").value,
      end: document.getElementById("end").value,
      category: document.getElementById("category").value
    })
  })
  .then(() => calendar.refetchEvents());
}
