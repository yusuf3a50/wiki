#this file should be placed at /home/$USER/
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"';
alias egrep='egrep --color=auto';
alias fgrep='fgrep --color=auto';
alias gitYusuf='git config user.name yusuf3a50 && git config user.email ybyphone@disroot.org';
alias grep='grep --color=auto';
alias l='ls -CF';
alias la='ls -A';
alias ll='ls -alF';
alias ls='ls --color=auto';
alias python='python3';
alias traf='nload -u K ifaceNAME';
alias up='sudo apt update && sudo apt upgrade -y';
alias ipt='sudo iptables -L -v';
alias fw='sudo ufw status verbose';
alias lsofpin='watch "sudo lsof -P -i -n"';