from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from models.event import add_event, get_all_events, update_event_time

calendar_bp = Blueprint("calendar", __name__)


@calendar_bp.route("/calendar")
@login_required
def calendar_view():
    return render_template("dashboard/calendar.html")



@calendar_bp.route("/api/events")
@login_required
def events():
    return jsonify(get_all_events(current_user.id))



@calendar_bp.route("/api/add-event", methods=["POST"])
@login_required
def create_event():
    data = request.get_json()

    color_map = {
        "College": "#7C3AED",
        "Medical": "#DC2626",
        "Personal": "#16A34A",
        "Meeting": "#2563EB"
    }

    add_event(
        current_user.id,
        data["title"],
        data["start"],
        data["end"],
        data["category"],
        color_map.get(data["category"], "#4F46E5")
    )

    return jsonify({"status": "success"})



@calendar_bp.route("/api/update-event", methods=["POST"])
@login_required
def update_event():
    data = request.get_json()
    update_event_time(data["id"], data["start"], data["end"])
    return jsonify({"status": "updated"})
