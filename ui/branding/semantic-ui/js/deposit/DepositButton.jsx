import * as React from 'react';
import Button from '@material-ui/core/Button';
import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';

export default function DepositButton() {
  const [anchorEl, setAnchorEl] = React.useState(null);
  const open = Boolean(anchorEl);
  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };
  const handleClose = () => {

    setAnchorEl(null);
  };

  return (
    <div>
      <Button
        variant='contained'
        aria-controls={open ? 'basic-menu' : undefined}
        aria-haspopup="true"
        aria-expanded={open ? 'true' : undefined}
        onClick={handleClick}
      >
        Deposit
      </Button>
      <Menu
        id="basic-menu"
        anchorEl={anchorEl}
        open={open}
        onClose={handleClose}
        MenuListProps={{
          'aria-labelledby': 'basic-button',
        }}
      >
        <a href="/mst/_new">
            <MenuItem onClick={handleClose}>MST</MenuItem>
        </a>
        <a href="/bli/_new">
            <MenuItem onClick={handleClose}>BLI</MenuItem>
        </a>
        <a href="/spr/_new">
            <MenuItem onClick={handleClose}>SPR</MenuItem>
        </a>
      </Menu>
    </div>
  );
}