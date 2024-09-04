# Referral-System-API


### Referral Reward 
Within our user database, we maintain two seprate columns:

- **`referral_code`**: Stores the referral code provided during registration.
- **`referral_id`**: Uniquely identifies each user. When a new user registers with an existing user's referral code, the system allocates reward points based on matching IDs.

### How It Works
1. A new user registers and provides a referral code.
2. The provided referral code is stored in the `referral_code` column.
3. The system matches this code with existing `referral_id` values.
4. If a match is found, the referring user receives reward points.


