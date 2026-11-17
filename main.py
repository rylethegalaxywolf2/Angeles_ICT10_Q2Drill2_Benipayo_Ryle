
from pyscript import document, when

grade7 = {"Bonnie Blue", "Gattouz Ponaldo", "Taro Canlas"}
grade8 = {"Mark Santos", "Fort nite", "Pirate Token"}
grade9 = {"Ben dover", "Justin Case", "Jack cool"}
grade10 = {"Shei Diaz", "Goo Ng", "Jerr King"}

all_members = grade7 | grade8 | grade9 | grade10


def display_members():
    member_list = document.querySelector("#member-list")
    member_list.innerHTML = ""

    for member in sorted(all_members):
        member_list.innerHTML += f"<li><span class='member-dot'></span>{member}</li>"

    document.querySelector("#count").innerText = str(len(all_members)) + " members"

    if len(all_members) == 0:
        document.querySelector("#empty-state").style.display = "block"
    else:
        document.querySelector("#empty-state").style.display = "none"


@when("click", "#add-member")
def add_member(event):
    first_name = document.querySelector("#first-name").value.strip()
    last_name = document.querySelector("#last-name").value.strip()

    if first_name == "" or last_name == "":
        document.querySelector("#message").innerText = "Enter both names."
        return

    new_member = first_name.title() + " " + last_name.title()

    if new_member in all_members:
        document.querySelector("#message").innerText = new_member + " already exists."
        return

    all_members.add(new_member)

    document.querySelector("#message").innerText = new_member + " added!"

    document.querySelector("#first-name").value = ""
    document.querySelector("#last-name").value = ""

    display_members()


display_members()
