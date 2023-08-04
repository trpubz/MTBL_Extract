# extract.rb
# Script that runs the all MTBL Extract system subprocesses
# @author: taylor.pubins
# modified: 04 AUG 2023
# v0.1.0

def build_scripts(dirs)
  """Builds an array of tuples containing the path to the python executable and the path to the script to run"""
  dir_hq = "/Users/Shared/BaseballHQ/tools"
  scripts = []
  dirs.each do |dir|
    scripts.append([File.join(dir_hq, "#{dir}/.venv/bin/python"), File.join(dir_hq, "#{dir}/main.py")])
  end
  scripts
end

def run_scripts(scripts)
  """Runs a script using the system command"""
  scripts.each do |dir, script|
    system(dir, script)
  end
end

def main
  # List of scripts to run
  scripts = build_scripts([
                            "Lg_Manager_Getter",
                            "Rosters_Getter",
                            "Fantasy_Data_Getter",
                            "Savant_Data_Getter",
                            "Fangraphs_Data_Getter"
                          ])

  run_scripts(scripts)
end

if __FILE__ == $0
  main
end
