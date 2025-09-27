export const assassins = [
    { name: "Anna",         kills: 0,   status: "in" },
    { name: "Anna Laura",   kills: 1,   status: "in" },
    { name: "Brielle",      kills: 0,   status: "in" },
    { name: "Ellie",        kills: 0,   status: "in" },
    { name: "Evelyn",       kills: 0,   status: "in" },
    { name: "Jack. H",      kills: 0,   status: "out" },
    { name: "Jackson",      kills: 0,   status: "in" },
    { name: "Jacob",        kills: 0,   status: "in" },
    { name: "Kai",          kills: 0,   status: "out" },
    { name: "Lola",         kills: 0,   status: "in" },
    { name: "Maeve",        kills: 1,   status: "in" },
    { name: "Phoenix",      kills: 0,   status: "in" },
    { name: "Presley",      kills: 0,   status: "in" },
    { name: "Sarah",        kills: 0,   status: "in" },
];

/**
 * Render the assassins table.
 * @param {string} containerId - The id of the UL container.
 * @param {object} options - Rendering options.
 * @param {boolean} options.showKills - Whether to show kills (default true).
 */
export function renderTable(containerId, options = { showKills: true }) {
    const list = document.getElementById(containerId);
    if (!list) return;
    list.innerHTML = "";

    const { showKills } = options;

    // Sort depending on whether kills matter
    assassins.sort((a, b) => {
        if (a.status !== b.status) return a.status === "out" ? 1 : -1;
        if (showKills && b.kills !== a.kills) return b.kills - a.kills;
        return a.name.localeCompare(b.name);
    });

    assassins.forEach(a => {
        const li = document.createElement("li");
        li.className = a.status;

        const nameSpan = document.createElement("span");
        nameSpan.textContent = a.name;
        nameSpan.className = "name";
        li.appendChild(nameSpan);

        if (showKills) {
            const killsSpan = document.createElement("span");
            killsSpan.textContent = a.kills;
            killsSpan.className = "kills";
            li.appendChild(killsSpan);
        }

        list.appendChild(li);
    });
}
