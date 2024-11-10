// original code found on https://github.com/LeoCroak/Ribbit-
// I made this with a bit of help
#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Inventory {
public:
    vector<string> items;

    void addItem(const string& item) {
        items.push_back(item);
    }

    void viewInventory() {
        if (items.empty()) {
            cout << "Your inventory is empty." << endl;
        } else {
            cout << "Your Inventory: " << endl;
            for (const auto& item : items) {
                cout << "- " << item << endl;
            }
        }
    }
};

int main() {
    Inventory inventory;
    string action, item;

    cout << "Welcome to the Simple Inventory System!" << endl;

    while (true) {
        cout << "Choose an action: 'add', 'view', or 'exit': ";
        cin >> action;

        if (action == "add") {
            cout << "Enter the item you want to add: ";
            cin >> item;
            inventory.addItem(item);
        } else if (action == "view") {
            inventory.viewInventory();
        } else if (action == "exit") {
            cout << "Exiting the inventory system." << endl;
            break;
        } else {
            cout << "Invalid action. Please enter 'add', 'view', or 'exit'." << endl;
        }
    }

    return 0;
}
