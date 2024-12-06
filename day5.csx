using System;
using System.Text.RegularExpressions;
using System.Collections.Generic;
using System.Linq;
var lines = Regex.Split(File.ReadAllText("input5.txt"), @"\n\n");
var rules = lines[0].Split('\n').Select(x => x.Split("|")).Select(l => (l[0], l[1]));
var updates = lines[1].Split('\n').Select(x => x.Split(","));

var parent_children = new Dictionary<string, List<string>>();
foreach ((string parent, string child) in rules){
    if(!parent_children.TryGetValue(parent, out var children)){
        children = new List<string>();
        parent_children[parent] = children;
    }
    parent_children[parent].Add(child);
}

string[] SortUpdate(string[] update)
{
    var number_of_children = new Dictionary<string, int>();
    foreach (var parent in update)
    {
        if (!parent_children.ContainsKey(parent))
        {
            number_of_children[parent] = 0;
            continue;
        }
        var children = parent_children[parent];
        var count = 0;
        foreach (var child in children)
        {
            if (update.Contains(child))
            {
                count++;
            }
        }
        number_of_children[parent] = count;
    }
    return update.OrderByDescending(x => number_of_children[x]).ToArray();
}

int IsCorrectUpdate(string[] update)
{
    var correct_order = SortUpdate(update);
    return update.SequenceEqual(correct_order) ? int.Parse(update[update.Length/2]) : 0;
}

var sorted = updates.Select(SortUpdate);
foreach (var update in sorted)
{
    Console.WriteLine(string.Join(",", update));
}
// Part 1
Console.WriteLine(updates.Select(IsCorrectUpdate).Sum());

// Part 2
var incorrect_updates = updates.Where(x => IsCorrectUpdate(x) == 0).ToList();
Console.WriteLine(incorrect_updates.Select(SortUpdate).Select(IsCorrectUpdate).Sum());
