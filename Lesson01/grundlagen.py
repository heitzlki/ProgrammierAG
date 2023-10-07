# %% [markdown]
# ## Aufgabe 1: print
#
# - Gebe in der Konsole "Hello World!" aus
#

# %%
print("Hello World!")

# %% [markdown]
# ## Aufgabe 2: variablen
#
# - Setze eine variable vom typ int und gebe sie in der Konsole aus. (z.B dein Alter)
# - Setze eine variable vom typ string und gebe sie in der Konsole aus. (z.B dein Name)
# - Setze eine liste und gebe sie in der Konsole aus (z.B deine Lieblingsgerichte)
# - Gebe folgende Ausgabe aus: Ich heiße [name] und bin [alter] Jahre alt und esse am liebsten [lieblingsgerichte]
#

# %%
alter = 17
name = "Kirill"
essen = ["pizza", "chicken nuggets", "mc flurry"]

print("Ich heiße", name, "und bin", alter, "Jahre alt und esse am liebsten", essen, ".")

# %% [markdown]
# ## Aufgabe 3: schleifen
#
# - Gebe in der Konsole deine Lieblingsgerichte aus.
# - Gebe deine Lieblingsgerichte in einer Zeile in der Konsole aus
#

# %%
for gericht in essen:
    print(gericht)

for i in range(len(essen)):
    print(i)
    print(essen[i])

i = 0
while i < len(essen):
    print(i)
    print(essen[i])
    i = i + 1

essen_string = ""
for gericht in essen:
    essen_string = essen_string + gericht + ", "

print(essen_string)

# %% [markdown]
# ## Aufgabe 4: if / else
#
# - Setze eine Variable fürs Alter und prüfe, ob eine Person alt genug für Alkohol ist
#

# %%
alter = 15

if alter >= 18:
    print("Du darfst jeden Alkohol trinken.")
elif alter >= 16:
    print("Du darfst Bier und Wein trinken.")
else:
    print("Du darfst keinen Alkohol trinken.")

# %% [markdown]
# ## Aufgabe 5: funktionen
#
# - Erstelle eine Funktion, die dein Alter mit einer zahl addiert und dann ausgibt.
# - Erstelle eine Funktion, die deinen Namen so oft ausgibt, wie du Jahre alt bist.
#


# %%
def alter_plus_zahl_print(alter, zahl):
    print(alter + zahl)


alter_plus_zahl_print(alter, 3)


def alter_plus_zahl_return(alter, zahl):
    return alter + zahl


print(alter_plus_zahl_return(alter, 4))

# %% [markdown]
# ## Aufgabe 6: user input
#
# - Erstelle eine Funktion, die deine Daten aufnimmt (alter, name, essen) und dies dann in der Konsole ausgibt.
#


# %%
def eingabe():
    alter = input("Alter: ")
    name = input("Name: ")
    essen = input("Lieblingsgerichte: ")

    print(
        "Ich heiße",
        name,
        "und bin",
        alter,
        "Jahre alt und esse am liebsten",
        essen,
        ".",
    )


eingabe()

# %% [markdown]
# ## Aufgabe 7: try / except
#
# - Modifiziere die Eingabe so, dass der Nutzer keinen Quatsch eingeben kann
#


# %%
def eingabe():
    try:
        alter = int(input("Alter: "))
    except:
        print("Bitte gib eine Zahl ein.")
        return None

    try:
        name = str(input("Name: "))
        if name == "":
            raise ValueError
    except:
        print("Bitte gib einen Namen ein.")
        return None

    try:
        essen = str(input("Lieblingsgerichte: "))
        if essen == "":
            raise ValueError
    except:
        print("Bitte gib ein Lieblingsgericht ein.")
        return None

    print(
        "Ich heiße",
        name,
        "und bin",
        alter,
        "Jahre alt und esse am liebsten",
        essen,
        ".",
    )


eingabe()
