# extract.rb
# Script that runs the all MTBL Extract system subprocesses
# @author: taylor.pubins
# modified: 04 AUG 2023
# v0.1.0

# Builds an array of tuples containing the path to the python executable and the path to the script to run
# .
# @param dirs [String] An array of the executable directories required for MTBL Extract
# @return scripts [[String, String]] An array of arrays. The first index of the inner array is the PATH of the binary
#   and the second index is the PATH to the main executable file
def build_scripts(dirs)
  dir_hq = "/Users/Shared/BaseballHQ/tools"
  scripts = []
  dirs.each do |dir|
    scripts.append([File.join(dir_hq, "#{dir}/.venv/bin/python"), File.join(dir_hq, "#{dir}/main.py")])
  end
  scripts
end

# Runs a script using the system command
#
# @param scripts [[String, String]] An array of arrays. The first index of the inner array is the PATH of the binary
#   and the second index is the PATH to the main executable file
# @return none
def run_scripts(scripts)
  threads = []
  executables = scripts
  first_two = executables.shift(2)
  # first two dependencies need to run first on their own thread
  threads << Thread.new do
    first_executable = first_two.shift
    second_executable = first_two.shift
    system(first_executable[0], first_executable[1])
    system(second_executable[0], second_executable[1])
  end
  # remaining executables can run on own threads
  executables.each do |dir, script|
    threads << Thread.new do
      system(dir, script)
    end
  end

  # Wait for all threads to complete
  threads.each(&:join)

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
